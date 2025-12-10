import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Optional
import asyncio

from app.core.config import settings
from app.core.decorators import handle_errors_async, handle_errors_sync


class SMTPEmailService:
    """
    Servicio para envío de emails vía SMTP.
    Configuración cargada desde app.core.config
    
    Variables de entorno necesarias (.env):
    - SMTP_HOST
    - SMTP_PORT
    - SMTP_USER
    - SMTP_PASSWORD
    - SMTP_FROM_EMAIL
    - SMTP_FROM_NAME (opcional)
    - SMTP_USE_TLS (opcional, default True)
    """
    
    def __init__(self):
        self.smtp_host = settings.SMTP_HOST
        self.smtp_port = settings.SMTP_PORT
        self.smtp_user = settings.SMTP_USER
        self.smtp_password = settings.SMTP_PASSWORD
        self.smtp_from = settings.SMTP_FROM_EMAIL
        self.smtp_from_name = getattr(settings, 'SMTP_FROM_NAME', 'Sistema Empresarial')
        self.use_tls = getattr(settings, 'SMTP_USE_TLS', True)
    
    def _parse_emails(self, emails: str) -> List[str]:
        """Convierte string de emails separados por coma a lista limpia"""
        if not emails:
            return []
        return [email.strip() for email in emails.split(',') if email.strip()]
    
    def _build_message(
        self,
        to_list: List[str],
        subject: str,
        body_html: str,
        cc_list: Optional[List[str]] = None
    ) -> MIMEMultipart:
        """Construye el mensaje MIME"""
        msg = MIMEMultipart('alternative')
        
        msg['Subject'] = subject
        msg['From'] = f"{self.smtp_from_name} <{self.smtp_from}>"
        msg['To'] = ', '.join(to_list)
        
        if cc_list:
            msg['Cc'] = ', '.join(cc_list)
        
        html_part = MIMEText(body_html, 'html', 'utf-8')
        msg.attach(html_part)
        
        return msg
    
    @handle_errors_sync
    def send_email(
        self,
        to: str,
        subject: str,
        body_html: str,
        cc: Optional[str] = None
    ) -> bool:
        """
        Envía un email de forma síncrona.
        
        Args:
            to: Emails destinatarios separados por coma "email1@x.com,email2@x.com"
            subject: Asunto del correo
            body_html: Contenido HTML del correo
            cc: Emails en copia separados por coma (opcional)
            
        Returns:
            bool: True si se envió exitosamente
        """
        to_list = self._parse_emails(to)
        cc_list = self._parse_emails(cc) if cc else None
        
        if not to_list:
            raise ValueError("Debe especificar al menos un destinatario")
        
        msg = self._build_message(to_list, subject, body_html, cc_list)
        
        all_recipients = to_list.copy()
        if cc_list:
            all_recipients.extend(cc_list)
        
        with smtplib.SMTP(self.smtp_host, self.smtp_port, timeout=30) as server:
            if self.use_tls:
                server.starttls()
            
            if self.smtp_user and self.smtp_password:
                server.login(self.smtp_user, self.smtp_password)
            
            server.send_message(msg, from_addr=self.smtp_from, to_addrs=all_recipients)
        
        return True
    
    @handle_errors_async
    async def send_email_async(
        self,
        to: str,
        subject: str,
        body_html: str,
        cc: Optional[str] = None
    ) -> bool:
        """
        Envía un email de forma asíncrona sin bloquear el event loop.
        
        Args:
            to: Emails destinatarios separados por coma
            subject: Asunto
            body_html: HTML del correo
            cc: Emails en copia (opcional)
            
        Returns:
            bool: True si se envió exitosamente
        """
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(
            None,
            self.send_email,
            to,
            subject,
            body_html,
            cc
        )
    
# Instancia singleton
email_service = SMTPEmailService()
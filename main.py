from app.core.email_service import email_service
if __name__ == "__main__":
    import asyncio
    
    html_alerta = """
    <html>
        <body>
            <h2>🚨 Alerta del Sistema</h2>
            <p>Se ha detectado una anomalía en el servidor.</p>
            <p><strong>Acción requerida:</strong> Revisar logs inmediatamente.</p>
        </body>
    </html>
    """
    
    # Uso síncrono
    try:
        success = email_service.send_email(
            to="admin@empresa.com,devops@empresa.com",
            subject="[ALERTA] Anomalía detectada",
            body_html=html_alerta,
            cc="supervisor@empresa.com"
        )
        print(f"✅ Email enviado: {success}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Uso asíncrono
    async def enviar_async():
        success = await email_service.send_email_async(
            to="admin@empresa.com",
            subject="[ALERTA] Test async",
            body_html=html_alerta
        )
        print(f"✅ Email async enviado: {success}")
    
    asyncio.run(enviar_async())
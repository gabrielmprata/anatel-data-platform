from anatel.core.logger import LoggerFactory

logger = LoggerFactory.create("BandaLargaPipeline")

logger.info("Pipeline iniciada.")
logger.info("Download iniciado.")
logger.warning("Arquivo muito grande.")
logger.error("Erro fictício para teste.")

print("Logger executado com sucesso!")

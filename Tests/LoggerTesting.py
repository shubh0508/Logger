from modules.Logger.NetBankingLogger import NetBankingLogger
nLogger = NetBankingLogger()

nLogger.info('mesg1', ['adffffa','fads'])
nLogger.info('mesg2', ['adffffa','fads'])
nLogger.info('mesg3', ['adffffa','fads'])

nLogger.error('mesg1', ['adffffa','fads'])
nLogger.error('mesg2', ['adffffa','fads'])
nLogger.error('mesg3', ['adffffa','fads'])

nLogger.fatal('mesg1', ['adffffa','fads'])


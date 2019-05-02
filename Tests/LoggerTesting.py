from modules.Logger.NetBankingLogger import NetBankingLogger
nLogger = NetBankingLogger()

nLogger.info('mesg1', ['adffffa','fads'])
nLogger.info('mesg2', ['adffffa','fads'])
nLogger.info('mesg3', ['adffffa','fads'])


q = nLogger._Logger__getQueue()

print(q.get())

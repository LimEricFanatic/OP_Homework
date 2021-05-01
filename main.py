import myLog
import logging

from Environment import Environment
from GASA import GASA

### 创建日志文件 ###
myLog.initLogging('myLog.log')
logging.info('Log Start!')

### 环境初始化 ###
env = Environment()
env.Initialize()
env.displayEnvironment()

### 遗传算法 ###
m_GASA = GASA(env, 50, 80, 0.4, 0.02, 1000, 1, 0.7)
m_GASA.Run()
m_GASA.Display()

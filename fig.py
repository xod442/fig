'''
 2017 wookieware.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


__author__ = "@netwookie"
__copyright__ = "Copyright 2017, wookieware."
__credits__ = ["Rick Kauffman"]
__license__ = "Apache2"
__version__ = "1.0.0"
__maintainer__ = "Rick Kauffman"
__email__ = "rick@rickkauffman.com"
__status__ = "Prototype"

Scripts sends full comware config to comware switch(es)
----------------------------------------------------------------------------------------------------
'''
from pyhpecommand.comware import HPCOM7
from pyhpecommand.features.config import Config
from pyhpecommand.features.booter import Booter
from pyhpecommand.features.reboot import Reboot
from multiprocessing import Process
from subprocess import Popen
import os

# python dict for coneecting to device
args = dict(host='192.168.19.130', username='admin', password='admin')
# tftp server ip address
server_ip ='192.168.19.128'
file_name ='my.cfg'
listx =['one']

# Connect to device
device = HPCOM7(**args)
device.open()
rick.append(fail)
# Create config class
fig = Config(device,file_name,server_ip)
# Build config
fig.build(stage=False)

#device.close()

print('New startup.cfg now on switch flash......')
#fig = Booter(device,file_name,server_ip)
# Build config

print('running booter')
#Popen(fig.bootbuild(stage=True))
bootname = 'rebootx.py'
basename = os.path.basename(bootname)
print basename
Popen(['/opt/dev_comware/rebootx.py'])
print('see ya')
exit()


#args = dict(reboot=True)
#booter = Reboot(device)
# Don't wait for the return
#thread.start_new_thread(booter.build(staged=False,**args))

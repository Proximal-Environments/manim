from manimlib import *

class Test(InteractiveScene):
    def construct(self):
        dot_grp = VGroup()
        for i in range(3):
            dot_grp.add(Dot())
        dot_grp.arrange()
        self.add(dot_grp)
        self.wait()
        self.remove_all_except(dot_grp[1])
        self.wait()

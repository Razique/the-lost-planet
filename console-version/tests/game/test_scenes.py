

class TestSceneManager(TestCase):
    def test_init(self):
        self.sm_init = scenes.SceneManager("test_scene")
        self.assertEqual(self.sm_init.next_scene, "test_scene")


class TestIntro(TestCase):
    def test_init(self):
        self.test_intro = scenes.Intro()
        self.assertEqual(self.test_intro.launcher(test="test_value"), "test_value")
        self.assertEqual(self.test_intro.action(test=True), "test_passed")


class TestTheBase(TestCase):
    def test_init(self):
        self.test_the_base = scenes.TheBase()
        self.assertEqual(self.test_the_base.launcher(test="test_value"), "test_value")
        self.assertEqual(self.test_the_base.action(base_first_decision="test_value"), "test_value")


class TestTheAlley(TestCase):
    def test_init(self):
        self.test_the_alley = scenes.TheAlley()
        self.assertEqual(self.test_the_alley.launcher(test="test_value"), "test_value")
        self.assertEqual(self.test_the_alley.action(test="test_value"), "test_value")


class TestTheCell(TestCase):
    def test_init(self):
        self.test_the_cell = scenes.TheCell()
        self.assertEqual(self.test_the_cell.launcher(test="test_value"), "test_value")
        self.assertEqual(self.test_the_cell.action(test="test_value"), False)


class TestThePipes(TestCase):
    def test_init(self):
        self.test_the_pipes = scenes.ThePipes()
        self.assertEqual(self.test_the_pipes.launcher(test="test_value"), "test_value")
        self.assertEqual(self.test_the_pipes.action(test=True), "test_passed")


class TestTheJetroom(TestCase):
    def test_init(self):
        self.test_the_jetroom = scenes.TheJetroom()
        self.assertEqual(self.test_the_jetroom.launcher(test="test_value"), "test_value")
        self.assertEqual(self.test_the_jetroom.chances, 3)


class TestRestart(TestCase):
    def test_init(self):
        self.test_restart = scenes.Restart()
        self.assertEqual(self.test_restart.launcher(test="test_value"), "test_passed")
        self.assertEqual(self.test_restart.action(test=True), "As Bastet, we believe you have 9 lives. Would you try again?")
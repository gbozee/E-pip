from click.testing import CliRunner
from . import mock, TestCase
from e_pip import cli, Project
import sys


class EpipInitializerTestCase(TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_init_help_functionality(self):
        result = self.runner.invoke(cli, ['--help'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("init", result.output) 
        self.assertIn("activate", result.output) 
        self.assertIn("generate", result.output) 
        self.assertIn("install", result.output) 
        self.assertIn("uninstall", result.output) 

    def test_init_has_a_method_to_determine_the_current_python_version(self):
        project = Project()
        version = sys.version_info
        python_version = "%s.%s" % (version.major, version.minor) 
        self.assertEqual(project.get_python_version(), python_version)
        self.assertEqual(project.get_python_version(major_version=True), version.major)

    def test_has_a_method_that_determines_whether_we_are_in_a_virtual_environment(self):
        project = Project()
        self.assertTrue(project.in_a_virtual_environment())

    def test_if_no_in_a_virtual_environment_installs_a_virtual_env(self):
        project = Project(virtual_environment=False)
        self.assertFalse(project.has_virtualenv_folder())
        with self.runner.isolated_filesystem():
            output = project.create_virtual_environment()
            self.assertEqual(output, 0)
            self.assertTrue(project.has_virtualenv_folder())

        

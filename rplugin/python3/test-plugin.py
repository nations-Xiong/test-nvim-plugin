import pynvim


@pynvim.plugin
class Main():
    def __init__(self, vim):
        self.vim = vim

    @pynvim.function('DoItPython')
    def DoItPython(self, args):
        self.vim.command('echo "hello from DoItPython"')

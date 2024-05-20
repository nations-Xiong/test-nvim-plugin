import neovim


@neovim.plugin
class Main():
    def __init__(self, vim):
        self.vim = vim

    @neovim.function('DoItPython')
    def DoItPython(self, args):
        self.vim.command('echo "hello from DoItPython"')

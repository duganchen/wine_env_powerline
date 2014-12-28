wine_env_powerline
==================

[Powerline](https://github.com/powerline/powerline) extension for [wine_env](https://github.com/duganchen/wine_env).

In your .zshrc, disable wine_env's standard prompt.

    export WINE_ENV_DISABLE_PROMPT=1

Then add the following to your Powerline shell theme's segments dictionary.
If you've left as much at default as possible, then it's in ~/.config/powerline/themes/shell/default.json:

    {"function": "wine_env_powerline.env.bottle"}

Then add the bottle to the "groups" section of your your color scheme. This file
is probably at ~/.config/powerline/colorschemes/shell/default.json:

	"bottle": { "fg": "white", "bg": "darkestpurple", "attr": ["bold"] }

Commands that put you in a bottle environment will now add the environment to your prompt. It will
be in white text, on a wine-colored background.

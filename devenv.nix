{
  languages.python = {
    enable = true;
    poetry.enable = true;
  };

  processes = {
    bot.exec = "poetry run python -m bingo-bot";
  };
}

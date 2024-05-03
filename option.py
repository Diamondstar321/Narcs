class Option:
  def __init__(self, prompt: str, action: str):
      """
      An option within a menu.
      :param prompt:  The text to tell the user what that selection will do.
      :param exec:    The code to be executed in response to that menu select.
      """
      self.prompt = prompt
      self.action = action

  def get_prompt(self):
      return self.prompt

  def get_action(self):
      return self.action

  def __str__(self):
      return "prompt {prompt} calls for {action}".format(prompt=self.prompt,
                                                         action=self.action)

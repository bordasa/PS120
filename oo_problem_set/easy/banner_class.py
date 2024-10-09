class Banner:
    def __init__(self, message, width = None):
        self.message = message

        if width == None:
            self.width = len(self.message)
        elif width >= 2:
            self.width = width - 2  #-2 to account for the minimum buffer that is hard-coded
        else:
            raise ValueError("Banner width must be at least 2")

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        return "| " + " " * self.width + " |"
    
    def _horizontal_rule(self):
        
        return "+-" + "-" * self.width + "-+"

    def _message_line(self):
        if len(self.message) == self.width:
            return f"| {self.message} |"
        
        elif len(self.message) < self.width:
            return self._create_short_line(self.message)
            
        else:
            full_lines, short_line_len = divmod(len(self.message), self.width)
            split_message_list = []

            for multiplier in range(1, full_lines + 1):
                start = self.width * (multiplier - 1)
                end = self.width * multiplier
                split_message_list.append(self.message[start: end])
            
            final_message_list = [f"| {line} |" for line in split_message_list]

            if short_line_len != 0:
                last_line = self._create_short_line(self.message[-short_line_len :])
                final_message_list += [last_line]

            return "\n".join(final_message_list)
    
    def _create_short_line(self, text):
        extra_space = self.width - len(text)
        left_padding = " " * (extra_space // 2)

        if extra_space % 2 == 1:
            right_padding = left_padding + " "
        else:
            right_padding = left_padding

        return f"| {left_padding}{text}{right_padding} |"


    
# Comments show expected output

banner = Banner('To boldly go where no one has gone before.', 20)
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('', 1)
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+
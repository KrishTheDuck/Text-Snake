import math as m


class Caterpillar:
    @staticmethod
    def linear_print(w: str, level: int, o: int) -> str:
        """
        print a absolute-value-waved text snake
        @param w: the string to snake-ify
        @param level: the highest number of spaces
        @param o: the total number of oscillations
        @return: a linear snake string
        """
        return "\n".join(["\n".join(" " * i + w
                                    for i in [abs(j) for j in range(-int(level / 2), int(level / 2))])
                          for _ in range(o)])

    @staticmethod
    def sin_print(w: str, x_scale: int, amp: int, level: int) -> str:
        # i never skip list comprehension day -colinhartigan
        # nerd -krish
        """
        print a sin-waved text snake
        @param w: the string to snake-ify
        @param x_scale: the horizontal compression factor
        @param amp: the amplitude of the sine wave
        @param level: how many lines to print
        @return: a sin snake string
        """
        return "\n".join(" " * i + w for i in [
            round(amp * (m.sin((1 / x_scale) * j)) + amp) for j in range(int(level * 2 * m.pi * x_scale))
        ])

    @staticmethod
    def helix_print(w: str, x_scale: int, amp: int, level: int) -> str:
        """
        print a helix-waved text snake
        @param w: the string to snake-ify
        @param x_scale: the horizontal compression factor
        @param amp: the amplitude of the sine wave
        @param level: how many lines to print
        @return: a helix snake string
        """
        return "\n".join(
            round(amp * (m.sin((1 / x_scale) * i + m.pi)) + amp) * " "
            + w +
            (
                (round(amp * (m.sin((1 / x_scale) * i)) + round(amp * (m.sin((1 / x_scale) * i)) + amp))) * " " + w
                if (round(amp * (m.sin((1 / x_scale) * i)) + round(amp * (m.sin((1 / x_scale) * i)) + amp)) > 0)
                else w[abs(round(amp * (m.sin((1 / x_scale) * i)) + round(amp * (m.sin((1 / x_scale) * i)) + amp))):4]
            )
            for i in [j for j in range(int(level * 2 * m.pi * x_scale))])

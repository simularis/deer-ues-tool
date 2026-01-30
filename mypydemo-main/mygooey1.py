import myscript
from gooey import Gooey

def main_gooey(inargs: list = None):
    # Create a new function based on the function that constructs ArgumentParser.
    # This is an alternative to the @Gooey decorator.
    f = Gooey(
            myscript.main,
            terminal_font_family='Consolas',
            progress_regex=r'Overall progress: (\d+)/(\d+)$',
            progress_expr='x[0] / x[1] * 100',
            hide_progress_msg=True,
            timing_options={
                'show_time_remaining':True,
                'hide_time_remaining_on_complete':False
            }
        )
    # Execute the function.
    # With inargs = None, default is to read sys.argv.
    f(inargs, use_tqdm=False)

if "__main__" == __name__:
    main_gooey()

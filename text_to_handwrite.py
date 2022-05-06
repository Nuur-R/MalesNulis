from pywhatkit import text_to_handwriting as kit


def text_to_handwriting(text, save_to):
    """Convert text to handwriting using pywhatkit"""
    kit(text, save_to="static/img/"+save_to+".png")
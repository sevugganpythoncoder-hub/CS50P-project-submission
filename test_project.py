from project import evaluate_toss, clean_path_input, format_host_display

def test_evaluate_toss():
    assert evaluate_toss("heads", "heads") == "Win"
    assert evaluate_toss("tails", "heads") == "Lose"

def test_clean_path_input():
    assert clean_path_input("C:\\Users\\Sevuggan\\   ") == "C:\\Users\\Sevuggan"
    assert clean_path_input("Downloads/ ") == "Downloads"

def test_format_host_display():
    assert format_host_display("desktop-pci") == "DESKTOP-PCI"
    assert format_host_display("  my-pc  ") == "MY-PC"
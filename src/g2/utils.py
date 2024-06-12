default_browser_options = {
    "block_images": True,
    "reuse_driver": True,
    "keep_drivers_alive": True,
    "close_on_crash": True,  # When Ready for Production change to True
    "headless": True,        # When Ready change to True
    'output': None,
}

default_request_options = {

    "raise_exception": False,
    "create_error_logs": False,
    "close_on_crash": True,  # When Ready for Production change to True
    "output": None,  # When Ready for Production Uncomment

}

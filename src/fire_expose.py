import fire

try:
    from src import utils
except ImportError:
    import utils

if __name__ == "__main__":
    fire.Fire({
        "greet": utils.greet,
        "goodbye": utils.goodbye,
    })

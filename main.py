import requests


# Example method for profiling
# def simple_request():
#     try:
#         requests.get("https://www.youtube.com")
#     except:
#         print("Website can't be reached at the moment")

def main():
    import cProfile
    import pstats
    with cProfile.Profile() as cp:
        # Program run method
        # simple_request()
        pass

    stats = pstats.Stats(cp)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()


if __name__ == '__main__':
    main()

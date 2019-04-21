import asyncio
import datetime


async def find_divisible(in_range, div_by):
    print("finding nums in range {} divisible by {}".format(in_range, div_by))
    located = []
    for i in range(in_range):
        if i % div_by == 0:
            located.append(i)
        # if i % 500000 == 0:
        #     await  asyncio.sleep(0.0001)
    print("Done w/ nums in range {} divisible by {}".format(in_range, div_by))
    return located


async def runner():
    # Creating task in the event loop.
    # When doing async programming the task should include high IO nor its not of much use.
    divs1 = event_loop.create_task(find_divisible(50800000, 34113))
    divs2 = event_loop.create_task(find_divisible(100052, 3210))
    divs3 = event_loop.create_task(find_divisible(500, 3))
    # Await for all the task to be complete
    # Await is much needed, nor we may call many co routines very quickly
    await asyncio.wait([divs1, divs2, divs3])
    return divs1, divs2, divs3


if __name__ == "__main__":
    time = datetime.datetime.now()
    try:
        # Create the event loop.
        event_loop = asyncio.get_event_loop()
        # Run the event loop and wait until complete
        d1, d2, d3 = event_loop.run_until_complete(runner())
        # Access individual results
        print(d1.result())
    except Exception as e:
        pass
    finally:
        try:
            # Don't forget to close the loop
            event_loop.close()
        except Exception as e:
            pass
    print("Elapsed", datetime.datetime.now() - time)


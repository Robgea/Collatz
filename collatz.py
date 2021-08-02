import sys
import datetime

def collatz_func(num, check_set):
    cleared_set = set()

    cleared = False

    while cleared == False:

        if num == 1:
            cleared_set.add(1)
            #sys.stdout.write("Found 1!\n")
            #sys.stdout.flush()
            return cleared_set

        if num in check_set:
            #sys.stdout.write(f"Num is in the cleared set! {num}. We're good to go! \n")
            #sys.stdout.flush()
            return cleared_set

        elif (num % 2) == 0:
            #sys.stdout.write(f'{num} is new and even! Dividing by two!\n')
            #sys.stdout.flush()
            cleared_set.add(num)
            num = num/2

        else:
            #sys.stdout.write(f'{num} is new and odd! 3X+1 time! {(num * 3) + 1}\n')
            cleared_set.add(num)
            num = (num * 3) + 1

    return cleared_set









def runner(target):

    sys.stdout.write(f"Starting hunt! \n \n Time is now: {datetime.datetime.now()}\n")

    start_time = datetime.datetime.now()

    confirmed_set = set()
    double_set = set()
    check_num = 1
    run_num = 1

    while run_num <= target:
        if check_num in confirmed_set:
            '''sys.stdout.write(f'Not checking {check_num}. Previously cleared!\n')
            sys.stdout.flush()'''
            check_num += 1

        elif check_num in double_set:
            confirmed_set.add(check_num)
            run_num += 1
            check_num += 1


        else:
            cleared_nums = collatz_func(check_num, confirmed_set)
            confirmed_set = confirmed_set|cleared_nums
            if run_num % 100 == 0:
                sys.stdout.write(f"Just finished run number: {run_num}! \n Checking: {check_num} \n New numbers are: {cleared_nums} \n \n Time is now: {datetime.datetime.now()}\n")
                sys.stdout.flush()

            if (check_num * 2) not in confirmed_set:
                double_set.add(check_num * 2)

            run_num += 1
            check_num += 1

    end_time = datetime.datetime.now()

    sys.stdout.write(f"Completed! \n Last number checked: {check_num} \n Total numbers checked: {len(confirmed_set)} \n Time is now: {datetime.datetime.now()} \n \n Start time was: {start_time} \n End time was: {end_time} \n Total runtime: {end_time - start_time}")
    sys.stdout.flush()


def main():
    runner(100_000)

if __name__ == '__main__':
    main()










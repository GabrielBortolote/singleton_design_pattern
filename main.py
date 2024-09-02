from click_counter import ClickCounter

if __name__ == '__main__':
    # click counter 1
    click_counter_1 = ClickCounter()
    for _ in range(0, 10):
        click_counter_1.click()

    print(f'{click_counter_1.counter} clicks were counted.')

    # click counter 1
    click_counter_2 = ClickCounter()
    for _ in range(0, 10):
        click_counter_2.click()

    print(f'{click_counter_2.counter} clicks were counted.')
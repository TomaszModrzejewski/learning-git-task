import matplotlib.pyplot as plt
import connection



def drawDiagram(currency_code_from, currency_code_to, number_days):
    rate_list, dates_list = connection.getRateTable(currency_code_from, currency_code_to, number_days)
    if type(rate_list) == int:
        return rate_list
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=[10, 4])
    ax.plot(dates_list, rate_list, color="green")
    plt.xlabel('Day')
    if number_days >= 6:
        if number_days != 9 and number_days != 10 and number_days != 11 and number_days != 17:
            plt.xticks(dates_list[::number_days//6], dates_list[::number_days//6])
        elif number_days != 9:
            plt.xticks(dates_list[::number_days // 5], dates_list[::number_days // 5])
        else:
            plt.xticks(dates_list[::number_days // 4], dates_list[::number_days // 4])
    plt.ylabel(str(currency_code_from) + '/' + str(currency_code_to))
    plt.show()

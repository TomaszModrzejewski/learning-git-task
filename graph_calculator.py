#import modules
import tkinter as tk
import sympy as sym

def get_input():
    function = function_entry.get()
    start = start_entry.get()
    end = end_entry.get()

    #edit input
    old_symbol = ['^','exp','log','sqrt','sin','cos','tan','sec','csc','cot','pi']
    new_symbol = ['**','sym.exp','sym.log','sym.sqrt','sym.sin','sym.cos','sym.tan','sym.sec','sym.csc','sym.cot','sym.pi']
    for i in range(len(old_symbol)):
        function = function.replace(old_symbol[i],new_symbol[i])
        start = start.replace(old_symbol[i],new_symbol[i])
        end = end.replace(old_symbol[i],new_symbol[i])
    
    return(function,start,end)

def draw_graph():
    #get all inputs
    global plot_function
    function, start, end = get_input()

    #draw function
    function = eval(function)
    if plot_function is None:
        if len(start) == 0 or len(end) == 0:
            plot_function = sym.plot(function, show = False)
        else:
            start = eval(start)
            end = eval(end)
            plot_function = sym.plot(function, (x,start,end), show = False)
    else:
        if len(start) == 0 or len(end) == 0:
            plot_new_function = sym.plot(function, show = False)
        else:
            start = eval(start)
            end = eval(end)
            plot_new_function = sym.plot(function, (x,start,end), show = False)
        plot_function.append(plot_new_function[0])
    plot_function.show()

def draw_implicit_graph():
    #get all inputs
    global plot_function
    function, start, end = get_input()

    #draw function
    function = eval(function)
    if plot_function is None:
        if len(start) == 0 or len(end) == 0:
            plot_function = sym.plot_implicit(function, show = False)
        else:
            start = eval(start)
            end = eval(end)
            plot_function = sym.plot_implicit(function, (x,start,end), show = False)
    else:
        if len(start) == 0 or len(end) == 0:
            plot_new_function = sym.plot_implicit(function, show = False)
        else:
            start = eval(start)
            end = eval(end)
            plot_new_function = sym.plot_implicit(function, (x,start,end), show = False)
        plot_function.append(plot_new_function[0])
    plot_function.show()

def draw_constant_graph():
    #get all inputs
    global plot_function
    function, start, end = get_input()

    #draw function
    function = eval(function)
    if plot_function is None:
        if len(start) == 0 or len(end) == 0:
            plot_function = sym.plot_implicit(function, y_var = x,show = False)
        else:
            start = eval(start)
            end = eval(end)
            plot_function = sym.plot_implicit(function, (x,start,end), y_var = x, show = False)
    else:
        if len(start) == 0 or len(end) == 0:
            plot_new_function = sym.plot_implicit(function, y_var = x, show = False)
        else:
            start = eval(start)
            end = eval(end)
            plot_new_function = sym.plot_implicit(function, (x,start,end), y_var = x, show = False)
        plot_function.append(plot_new_function[0])
    plot_function.show()

def clear_graph(clear_option=None):
    global plot_function
    plot_function = None

#create main window
main_window = tk.Tk()
main_window.title("Graph Calculator")

#create input widget
frame1 = tk.Frame(master = main_window)
function_label = tk.Label(master = frame1, text = 'Function')
function_entry = tk.Entry(master = frame1)
start_label = tk.Label(master = frame1, text = 'Start')
start_entry = tk.Entry(master = frame1)
end_label = tk.Label(master = frame1, text = 'End')
end_entry = tk.Entry(master = frame1)

#positioning input widget
frame1.pack()
function_label.grid(row = 0, column = 0)
function_entry.grid(row = 0, column = 1)
start_label.grid(row = 0, column = 2)
start_entry.grid(row = 0, column = 3)
end_label.grid(row = 0, column = 4)
end_entry.grid(row = 0, column = 5)

#create button widget
frame2 = tk.Frame(master = main_window)
draw_button = tk.Button(
    master = frame2,
    text = 'Draw',
    command = draw_graph
)
draw_implicit_button = tk.Button(
    master = frame2,
    text = 'Draw Implicit',
    command = draw_implicit_graph
)
draw_constant_button = tk.Button(
    master = frame2,
    text = 'Draw Constant',
    command = draw_constant_graph
)
clear_button = tk.Button(
    master = frame2,
    text = 'Clear',
    command = clear_graph
)

#positioning button widget
frame2.pack()
draw_button.grid(row = 0, column = 0)
draw_implicit_button.grid(row = 0, column = 1)
draw_constant_button.grid(row = 0, column = 2)
clear_button.grid(row = 0, column = 3)

#some global variables
plot_function = None
x,y = sym.symbols('x y')

main_window.mainloop()
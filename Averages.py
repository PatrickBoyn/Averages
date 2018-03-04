"""Average number program"""
import psycopg2
import itertools

#weight_id, weight, date_created
# Enter a, q  or a number to the database.
print("Please enter h, or H for help, otherwise enter a number:  ")
AVERAGES = input()

# connect to the database. 
try:
    CONN = psycopg2.connect("dbname='averages' user='postgres' host='localhost'")
    CUR = CONN.cursor()
except psycopg2.OperationalError as e:
    print("No database by that name exists.")


def main():
    # Checks for h, H, or a number.
       pass
       
        # if AVERAGES == "a":
        #     get_averages()
        #     CONN.close()
        # elif AVERAGES == "q":
        #     leave()
        #     CONN.close()
        # elif AVERAGES == "w":
        #     list_weights()
        #     get_date()
        #     CONN.close()
        # elif AVERAGES == "d":
        #     weight_change()
        #     CONN.close()
        # elif AVERAGES == type(32) or type(32.5):
        #     insert_weight()
        #     CONN.close()
        # else:
        #     print("Please type a, q, w, d or a number.")
        #     CONN.close()


def logic_loop():
       if AVERAGES == type(1) or type(.4):
            insert_weight()
       elif AVERAGES == "h" or "H":
           help()
       elif AVERAGES == "q" or "Q":
           leave()
       else:
            print("Please enter H/h or a number. ")
def insert_weight():
    #Inserts the value of the number entered into the average database.
    psql = "INSERT INTO averages(weight, date_created) values(%s, CURRENT_DATE)" % float(AVERAGES)
    CUR.execute(psql)
    CONN.commit()


def get_date():    
    psql8 = "SELECT date_created FROM averages"
    CUR.execute(psql8)
    results4 = CUR.fetchall()
    unpacked, = results4[0]

    if unpacked == None:
        print("Still nothing here.")
    else:
        print(unpacked)


def get_averages():
    # Where the averge numbers are acquired from. It's much faster than doing it in Python.
    psql2 = "SELECT avg(weight) FROM averages"
    CUR.execute(psql2)
    results = CUR.fetchall()

    # Unpacks the tuples so it reads as a number rather than a list of tuples.
    av,  = results[0]

    # Prints the results of the average numbers. 
    print("This is the average of all the weights entered: ")
    print(round(av, 1))
    return results


def list_weights():
    # Grabs all of the numbers entered into the database.
    psql3 = "SELECT weight FROM averages"
    CUR.execute(psql3)
    results1 = CUR.fetchall()

    # Makes the list of results look nicer in the console
    unpack_results = itertools.chain(*results1)
    results_as_strings = map(str, unpack_results)
    formatted_results = ', '.join(results_as_strings)

    #Prints the results.
    print("Here is the list of weights you entered: ")
    print(formatted_results)

def two_recents():
    #subtracts the most recent weights from each other
    psql6 = "SELECT weight FROM averages ORDER BY weight_id DESC limit 1 offset 1"
    psql7 = "SELECT max(weight) FROM averages LIMIT 1"
    CUR.execute(psql6)
    results6 = CUR.fetchall()
    CUR.execute(psql7)
    results7 = CUR.fetchall()
    a, = results6[0]
    b, = results7[0]
    diff = b -a
    print(diff) 


def weight_change():
    # Grabs the first and last number from the averages list.
    psql4 = "SELECT min(weight) FROM averages LIMIT 1"
    psql5 = "SELECT max(weight) FROM averages LIMIT 1"
    CUR.execute(psql4)
    results2 = CUR.fetchall()
    CUR.execute(psql5)
    results3 = CUR.fetchall()

    # Unpacks the tuples so the difference can be returned from them.
    a,  = results2[0]
    b, = results3[0]
    diff = b - a

    print("The difference between highest and lowest weight was: \n " + str(round(diff, 1)))

    # For Testing purposes. 
    print("The two numbers subtracted were: ")
    difference = str(a) + ", " + str(b)
    print(difference)
    return diff


def leave():
    # Exits the program with a message.
    print("See you next time!")
    quit()


def help():
    # Prints the various things you can do with this program. 
    print("Here are your options: ")
    print("Press a for weight averages.")
    print("Press q to quit the program.")
    print("Press w to list the weights in the database. ")
    print("Press d to find the difference between the biggest and smallest weights.")
    print("Press r to find the difference between the most recent weights. ")


# I prefer methods and functions at the bottom of files. This is the Python way of handling that.
if  __name__ == "__main__":
    try:
        main()
    except NameError as e:
        print("No variable by that name exists."+ "\n"+ str(e))
  
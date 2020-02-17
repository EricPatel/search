import fire
import map

def main():    
    number_of_runs = 20
    dim = 10
    p = 0.3
    for q in range(0, 110, 10):
        strategy1_successes = 0
        strategy2_successes = 0
        strategy3_successes = 0
        for i in range(number_of_runs):
            fireG = fire.generateFireMap(dim, p)
            result1 = fire.strategy1(fireG, q/100)
            result2 = fire.strategy2(fireG, q/100)
            result3 = fire.strategy3(fireG, q/100)

            if result1 != "Failure: No Path":
                strategy1_successes = strategy1_successes + 1

            if result2 != "Failure: No Path":
                strategy2_successes = strategy2_successes + 1
            
            if result3 != "Failure: No Path":
                strategy3_successes = strategy3_successes + 1

        print("Strategy 1 with q = " + str(q/100))
        print("Average Success Rate: " + str(strategy1_successes/number_of_runs))
        print("")
        print("Strategy 2 with q = " + str(q/100))
        print("Average Success Rate: " + str(strategy2_successes/number_of_runs))
        print("")
        print("Strategy 3 with q = " + str(q/100))
        print("Average Success Rate: " + str(strategy3_successes/number_of_runs))
        print("")

if __name__ == "__main__":
    main()
import re

def exchange_names():
    print("Let's exchange our names.\nFirst ask me")
    names=""
    while True:
        try:
            user_in = input("--> ")
            if re.search(r"^(what is|what's|whats) your name(\s+)?\?$",user_in,flags=re.IGNORECASE):
                print("I'm Cyrus. What's your name ?")
                answer_in = input("--> ")
                #answer_in = answer_in.lower()
                if match:=re.search(r"^(i\s+a?m|i'm|iam)\s+(.+)$",answer_in,flags=re.IGNORECASE):
                    print(f"Hello {match.group(2)}")
                    names=match.group(2)
                else:
                    print(f"Hello {answer_in}")
                    names=answer_in
                break

        except re.error:
            print("Let exchange our names.\nFirst ask me")

        except Exception:
            print("Custom error:")
            raise  # Re-raise the exception to propagate it further if needed
        except Exception:
            print("An unexpected error occurred:")


    return names

def Greet():
    print("How are you ?")
    response = []
    while True:
        try:
            user_in = input("--> ")
            if re.search(r"^(fine|i\s+am\s+fine|i\s+am\s+good|good)$", user_in, flags=re.IGNORECASE):
                response.append(user_in)
                print("What do you plan to do ?")
                answer_in = input("--> ")
                # answer_in = answer_in.lower()
                if answer_in:
                    print("We will look into it.")
                    response.append(answer_in.strip())
            else:
                print("Think about tomorrow")

        except re.error:
            print("Check grammar\n")

        except Exception:
            print("An unexpected error occurred:")
        else:
            break
    return response

def Intro():
    print("You are a human.\nRight ?")
    responses = []
    while True:
        try:
            user_in = input("--> ")
            if re.search(r"^(yes|yupp|right)$", user_in, flags=re.IGNORECASE):
                print("I'm Cyrus. An AI")
                responses.append(user_in.strip())
                answer_in = input("--> ")
                # answer_in = answer_in.lower()
                if answer_in:
                    responses.append(answer_in.strip())
            else:
                print("Aliens are troublesome")


        except re.error:
            print("Check grammar\n")


        except Exception:
            print("An unexpected error occurred:")
        else:
            return responses
def main():
    print("It's cyrus")

    user_name = exchange_names()
    greet = Greet()
    intro = Intro()

if __name__ == "__main__":
    main()



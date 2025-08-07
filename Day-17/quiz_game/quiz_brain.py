class QuizBrain:
    def __init__(self,q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score =0

    
    def check_ans(self,user_answer,correct_answer):
        if user_answer.lower() ==correct_answer.lower():
            print("You got it rigth!")
            self.score+=1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.q_number}")
        print("\n")

        


    def still_has_question(self):
        return (len(self.q_list)>self.q_number)   
    
    def next_question(self):
        current_question = self.q_list[self.q_number]
        print(type(current_question))
        self.q_number+=1
        user_answer = input(f"Q.{self.q_number}: {current_question.question} (True/False):\n")
        self.check_ans(user_answer,current_question.answer)

  
    def finish(self):
        print("You've completed the quiz.")
        print(f"Your final score was: {self.score}/{self.q_number}")

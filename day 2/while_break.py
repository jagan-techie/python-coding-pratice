while True:
    user_input = input("Type 'exit' to stop the program: ").lower()
    
    if user_input == "exit":
        print("Goodbye!")
        break  # Forces immediate exit from the loop
        
    print(f"You typed: {user_input}")

try :
    k=2/3
except Exception as e:
    print("Exception caught in main:", e)
else:
    print(k)
finally:
    print("Execution completed.")
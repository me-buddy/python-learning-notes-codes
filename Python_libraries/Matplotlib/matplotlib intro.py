import numpy as np

import matplotlib.pyplot as plt


customer_names = np.array(["Manoj","Ram","Kanha","Rahul"])
purchasing = np.array([1000,3233,2121,600])

plt.bar(customer_names,purchasing)
plt.plot(customer_names,purchasing,marker="s",color="green",linewidth="3",linestyle="dashed",label="Customer_Sales")
plt.xlabel("Customer names")
plt.ylabel("Purchasing")
plt.title("Customer_Sales")
plt.legend()
plt.grid()



# ==================================================================


plt.show()
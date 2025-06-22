# 🛡️ Python URL Scanner  

A simple Python tool that scans and rates URLs based on various security checks.  

## 🚀 How It Works  
1. **Checks URL Reachability** – Ensures the URL is accessible online.  
2. **Blacklist Check** – If the URL is blacklisted, the program notifies the user and stops.  
3. **URL Breakdown** – Extracts and analyzes components (E.g https://fonts.google. com):
   - Protocol (e.g., `https`)  
   - Subdomain (e.g., `fonts`)  
   - Domain (e.g., `google`)  
   - TLD (e.g., `.com`)  
4. **Scanning & Rating** – Matches components against lists of suspicious protocols/domains and updates the risk rating.  
5. **Final Rating** – If the rating is **< 5**, the URL is added to the blacklist. 

## Usage
Clone or download the repository, then run the **Scanner.py** module. To get the best out of the tool use [Pycharm IDE!](https://www.jetbrains.com/pycharm/)  
You might have to install some modules i.e ```pip install requests``` 

## Reach Out
Feel free to extend your suggestions and collaboration to me:
- **🔗 LinkedIn:** [Tshepho M](www.linkedin.com/in/tshepho-madubanya-188aa3251)  

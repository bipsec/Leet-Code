class Solution:
    def numUniqueEmails(self, emails) -> int:
        newEmails = []
        names = []
        domains = []

        for i in range(len(emails)):
            items = emails[i].split("@")
            names.append(items[0])
            domains.append(items[1])

        for item in names:
            vals = ""
            for i in range(len(item)):
                if item[i] == ".":
                    continue
                elif item[i] == "+":
                    break
                else:
                    vals += item[i]
            names.append(vals)
            vals = ""
        
        Emails = []

        for i in range(len(newEmails)):
            form_emails = newEmails[i]+"@"+domains[i]
            Emails.append(form_emails)

        return len(set(Emails))
    

    def numUniqueEmails2(self, emails) -> int:
        unique_emails = set()

        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            unique_emails.add(local + '@' + domain)

        return len(unique_emails)
    
    # efficient version is number 2 - it was so simple, so elegant and looking like a wow :)



s = Solution()
print(s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
print(s.numUniqueEmails(emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))
print(s.numUniqueEmails(emails = ["a+@leetcode.com","a+vnisuer.bvsniuer@lee.tcode.com","c@leet.code.com"]))
print(s.numUniqueEmails(emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com", "b@leetcode.com","c@leetcode.com"]))
print(s.numUniqueEmails(emails = ["testemail@leetcode.com", "testemail@leet.code.com"]))
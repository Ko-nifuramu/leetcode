from typing import List



#time: O(len(emails)*len(email))
#space: O(len(emails))
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid_email_set = set([])
	
        def is_valid_email(email):
            if not ('@' in email):
                return False
            at_index = email.index('@')
            if '.com' in email[at_index:]:
                return True
            return False
            
        for email in emails:
            if not is_valid_email:
                continue
            at_index = email.index('@')
            local_name = email[:at_index]
            domain_name = email[at_index+1:]
            index = 0
            while index < len(local_name):
                if local_name[index] == '.':
                    local_name = local_name[:index] + local_name[index+1:]
                    continue
                if local_name[index] == '+':
                    local_name = local_name[:index]
                    break
                index += 1
            
            valid_email_set.add(local_name + '@' + domain_name)
        
        return len(valid_email_set)


#time: O(len(emails)*len(email))
#space: O(len(emails))
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local_part, domain = email.rsplit('@', maxsplit = 1)
            local_part_filtered = local_part.split('+')[0].replace('.', '')
            unique_emails.add(f"{local_part_filtered}@{domain}")
        return len(unique_emails)


#time: O(len(emails)*len(email))
#space: O(len(emails))
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            at_mark_index = email.index('@')
            local_part= email[:at_mark_index]
            domain  = email[at_mark_index:]#"@" is contained
            local_name = ''
            for c in local_part:
                if c == '.':
                    continue
                if c == '+':
                    break
                local_name += c
            
            unique_emails.add(local_name + domain)
        
        return len(unique_emails)
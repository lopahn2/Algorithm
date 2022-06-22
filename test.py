def solution(id_list, report, k):
    answer = []
    reportMember = {}
    reportedMember = {}
    reportLog = []
    for member in id_list:
        reportMember[member] = 0
        reportedMember[member] = 0
        
    for reportInfo in report:
        reporter, reportee = reportInfo.split()
        reportLog.append((reporter, reportee))
    reportLog = list(dict.fromkeys(reportLog))
    
    for rep in reportLog:
        reportedMember[rep[1]] += 1
        if reportedMember[rep[1]] % k == 0:
            for repInfo in reportLog:
                if repInfo[1] == rep[1]:
                    reportMember[repInfo[0]] += 1
    
    for reporter in reportMember.keys():
        answer.append(reportMember[reporter])

        
    return answer


def solution(id_list, report, k):
    reported_cnt = {x:0 for x in id_list}
    received_mail_cnt = [0] * len(id_list)
    
    for r in set(report):  # report 형식 : '이용자id 신고한id'
        reported_cnt[r.split()[1]] += 1
            
    for r in set(report):
        if reported_cnt[r.split()[1]] >= k:
            received_mail_cnt[id_list.index(r.split()[0])] += 1
    
    return received_mail_cnt
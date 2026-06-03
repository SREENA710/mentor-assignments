# Write a regex to extract `timestamp`, `level`, `user`, `endpoint`, `status`, and `latency_ms`
# 2026-05-20 10:15:22 ERROR user=alice endpoint=/api/payments status=500 latency_ms=842

r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+([A-Z]+)\s+([a-z]+)\s+([/A-Z]+)\s+(\d+)\s+(\d+)$"
r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+([A-Z]+)\s+user=([a-z]+)\s+endpoint=([/A-Z]+)\s+status=(\d+)\s+latency_ms=(\d+)$"


# Write a regex to extract `level`, `process`, `pid`, `queue`, `retry`, and `message`.
# WARN payment-worker pid=3421 queue=refunds retry=3 message="timeout calling bank gateway
r"^([A-Z]+)\s+([a-z-]+)\s+pid=(\d+)\s+queue=([a-z]+)\s+retry=(\d+)\s+message=\"(.+)\"$"


# Write a regex to extract `container`, `event`, `exit_code`, `reason`, and `image`.
# container=api-server event=die exit_code=137 reason=OOMKilled image=client-api:2026.05.20
r"^container=(\S+)\s+event=(\w+)\s+exit_code=(\d+)\s+reason=(\w+)\s+image=(\S+)$"


# Write a regex to extract `user`, `action`, `branch`, `target`, `result`, and `files`.
# git user=riya action=merge branch=feature/login target=main result=conflict files=3
r"^git\s+user=(\w+)\s+action=(\w+)\s+branch=(\S+)\s+target=(\w+)\s+result=(\w+)\s+files=(\d+)$"


# Write a regex to extract `ip`, `timestamp`, `method`, `path`, `status`, `bytes`, and `user_agent`.
# 10.2.4.8 -- [20/May/2026:10:21:09 +0000] "POST /api/orders HTTP/1.1" 201 342 "curl/8.1"
r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+--\s+"([A-Z]+)\s+(\S+)\s+"\s+(\d+)\s+(\d+)\s+"$'


# Write a regex to extract `timestamp`, `host`, `process`, `pid`, `attempted_user`, `source_ip`, and `source_port`.
# May 20 10:45:12 app-prod sshd[9214]: Failed password for invalid user admin from 203.0.113.9 port 51422 ssh2
r"^([A-Za-z]{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\S+)\s+$"
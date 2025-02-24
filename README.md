# Convert file excel to yaml then compare

# Điểm giống nhau:
Cơ bản giống nhau

# Điểm khác nhau:
- kubeadm.kubernetes.io/etcd.advertise-client-urls: https://172.1.1.112:2379
+ Trong etcd.yaml: hiển thị cả dòng như trên
+ Trong version_1_output.yaml: hiển thị mỗi dấu "." là 1 phân cấp

- spec.containers[0].command[0]
spec.containers[0].command[1]
...
+ Trong etcd.yaml: không cấp đánh chỉ số command
+ Trong version_1_output.yaml: phân cấp đánh chỉ số command như trên excel

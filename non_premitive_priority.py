class Priority:

    def processData(self, no_of_processes):
        process_data = []
        for i in range(1,no_of_processes+1):
            temporary = []
            
            arrival_time = int(input("Enter Arrival Time for Process {}: ".format(i)))

            burst_time = int(input("Enter Burst Time for Process {}: ".format(i)))

            priority = int(input("Enter Priority for Process {}: ".format(i)))

            temporary.extend([i, arrival_time, burst_time, priority, 0])
            
            process_data.append(temporary)
        Priority.schedulingProcess(self, process_data)


    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0
        process_data.sort(key=lambda x: x[1])
        
        for i in range(len(process_data)):
            ready_queue = []
            temp = []
            normal_queue = []
            for j in range(len(process_data)):
                if((process_data[j][1] <= s_time) and (process_data[j][4] == 0)):
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2], process_data[j][3]])
                    ready_queue.append(temp)
                    temp = []
                elif(process_data[j][4] == 0):
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2], process_data[j][3]])
                    normal_queue.append(temp)
                    temp = []
            if(len(ready_queue) != 0):
                ready_queue.sort(key=lambda x: x[3])
                
                start_time.append(s_time)
                s_time = s_time + ready_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                for k in range(len(process_data)):
                    if(process_data[k][0] == ready_queue[0][0]):
                        break
                process_data[k][4] = 1
                process_data[k].append(e_time)
            elif (len(ready_queue) == 0):
                if (s_time < normal_queue[0][1]):
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + normal_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                for k in range(len(process_data)):
                    if (process_data[k][0] == normal_queue[0][0]):
                        break
                process_data[k][4] = 1
                process_data[k].append(e_time)
        t_time = Priority.calculateTurnaroundTime(self, process_data)
        w_time = Priority.calculateWaitingTime(self, process_data)
        Priority.printData(self, process_data, t_time, w_time)


    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        
        return average_turnaround_time


    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][2]
            
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        
        return average_waiting_time


    def printData(self, process_data, average_turnaround_time, average_waiting_time):
        
        print("Process_ID  Arrival_Time  Burst_Time     Priority     Completion_Time    Turnaround_Time    Waiting_Time")
        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                if(j==4):
                    continue
                
                print(process_data[i][j], end="\t\t")
            print()
        print('Average Turnaround Time:',average_turnaround_time)

        print('Average Waiting Time:',average_waiting_time)
        
        print('Number of context switches:',no_of_processes-1)



no_of_processes = int(input("Enter number of processes: "))
priority = Priority()
priority.processData(no_of_processes)
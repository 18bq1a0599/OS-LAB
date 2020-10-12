class Priority:

    def processData(self, no_of_processes):
        process_data = []
        for i in range(1,no_of_processes+1):
            temporary = []
            

            arrival_time = int(input("Enter Arrival Time for Process {}: ".format(i)))

            burst_time = int(input("Enter Burst Time for Process {}: ".format(i)))

            priority = int(input("Enter Priority for Process {}: ".format(i)))

            temporary.extend([i, arrival_time, burst_time, priority, 0, burst_time])
            
            process_data.append(temporary)
        Priority.schedulingProcess(self, process_data)

    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_process = []
        process_data.sort(key=lambda x: x[1])
        
        while (1):
            ready_queue = []
            normal_queue = []
            temp = []
            for i in range(len(process_data)):
                if (process_data[i][1] <= s_time and process_data[i][4] == 0):
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][3],
                                 process_data[i][5]])
                    ready_queue.append(temp)
                    temp = []
                elif (process_data[i][4] == 0):
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4],
                                 process_data[i][5]])
                    normal_queue.append(temp)
                    temp = []
            if (len(ready_queue) == 0 and len(normal_queue) == 0):
                break
            if (len(ready_queue) != 0):
                ready_queue.sort(key=lambda x: x[3])
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(ready_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][2] = process_data[k][2] - 1
                if (process_data[k][2] == 0):       #if burst time is zero, it means process is completed
                    process_data[k][4] = 1
                    process_data[k].append(e_time)
            if (len(ready_queue) == 0):
                normal_queue.sort(key=lambda x: x[1])
                if (s_time < normal_queue[0][1]):
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(normal_queue[0][0])
                for k in range(len(process_data)):
                    if (process_data[k][0] == normal_queue[0][0]):
                        break
                process_data[k][2] = process_data[k][2] - 1
                if (process_data[k][2] == 0):        #if burst time is zero, it means process is completed
                    process_data[k][4] = 1
                    process_data[k].append(e_time)
        t_time = Priority.calculateTurnaroundTime(self, process_data)
        w_time = Priority.calculateWaitingTime(self, process_data)
        Priority.printData(self, process_data, t_time, w_time, sequence_of_process)

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][6] - process_data[i][1]
            
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        
        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][7] - process_data[i][5]
            
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        
        return average_waiting_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time, sequence_of_process):
       
        print("Process_ID  Arrival_Time    Priority     Burst_Time    Completion_Time   Turnaround_Time    Waiting_Time")
        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                if(j==2 or j==4):
                    continue

                print(process_data[i][j], end="\t\t")
            print()

        print('Average Turnaround Time:',average_turnaround_time)

        print('Average Waiting Time:',average_waiting_time)
        context_switch=0
        
        for i in range(len(sequence_of_process)-1):
            if(sequence_of_process[i]!=sequence_of_process[i+1]):
                context_switch+=1

        print('Number of context switches:',context_switch)



no_of_processes = int(input("Enter number of processes: "))
priority = Priority()
priority.processData(no_of_processes)
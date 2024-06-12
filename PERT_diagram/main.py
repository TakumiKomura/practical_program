from pertchart import PertChart

dataFilePath = r"C:\Users\Komura Takumi\Documents\programing\PracticalProgram\PERT_diagram\data.json"
pc = PertChart()
tasks = pc.getInput(dataFilePath)
# pc.create_pert_chart(pc.calculate_values(tasks))
pc.create_pert_chart(pc.calculate_values(tasks), font_name='MS Gothic')

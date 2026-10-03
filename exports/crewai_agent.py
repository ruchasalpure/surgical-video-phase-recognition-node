from crewai import Agent

surgical_video_phase_recognition_node = Agent(
    role="Surgical Video Phase Recognition Node",
    goal="Deliver high-precision autonomous Surgical Video Phase Recognition Node operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)

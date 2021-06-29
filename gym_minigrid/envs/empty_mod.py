from gym_minigrid.minigrid import *
from gym_minigrid.register import register

class EmptyEnv(MiniGridEnv):
    """
    Empty grid environment, no obstacles, sparse reward
    """

    def __init__(
        self,
        size=8,
        agent_start_pos=(1,1),
        agent_start_dir=0,
		goal_pos=(1,1),
    ):
        self.agent_start_pos = agent_start_pos
        self.agent_start_dir = agent_start_dir
		self.goal_pos = goal_pos

        super().__init__(
            grid_size=size,
            max_steps=4*size*size,
            # Set this to True for maximum speed
            see_through_walls=True
        )

    def _gen_grid(self, width, height):
        # Create an empty grid
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.wall_rect(0, 0, width, height)

		# Place the goal
        if self.goal_pos is not None:
			# Place a goal square in the bottom-right corner
        	self.put_obj(Goal(), width - 2, height - 2)
        else:
            # Place a goal square in a random place
        	#self.put_obj_rand(Goal(), width - 2, height - 2)
			#self.put_obj_rand(Goal(), width - 1, height - 1)
			self.put_obj_rand(Goal(), width, height)

        # Place the agent
        if self.agent_start_pos is not None:
            self.agent_pos = self.agent_start_pos
            self.agent_dir = self.agent_start_dir
        else:
            self.place_agent()

        self.mission = "get to the green goal square"

class EmptyEnv5x5(EmptyEnv):
    def __init__(self, **kwargs):
        super().__init__(size=5, **kwargs)

class EmptyRandomEnv5x5(EmptyEnv):
    def __init__(self):
        super().__init__(size=5, agent_start_pos=None)

class EmptyRandomRandomGoalEnv5x5(EmptyEnv):
    def __init__(self):
        super().__init__(size=5, agent_start_pos=None, goal_pos=None)

class EmptyRandomGoalEnv5x5(EmptyEnv):
    def __init__(self):
        super().__init__(size=5, goal_pos=None)

class EmptyEnv6x6(EmptyEnv):
    def __init__(self, **kwargs):
        super().__init__(size=6, **kwargs)

class EmptyRandomEnv6x6(EmptyEnv):
    def __init__(self):
        super().__init__(size=6, agent_start_pos=None)

class EmptyRandomRandomGoalEnv6x6(EmptyEnv):
    def __init__(self):
        super().__init__(size=6, agent_start_pos=None, goal_pos=None)

class EmptyRandomGoalEnv6x6(EmptyEnv):
    def __init__(self):
        super().__init__(size=6, goal_pos=None)

class EmptyRandomEnv8x8(EmptyEnv):
    def __init__(self):
        super().__init__(size=8, agent_start_pos=None)

class EmptyRandomRandomGoalEnv8x8(EmptyEnv):
    def __init__(self):
        super().__init__(size=8, agent_start_pos=None, goal_pos=None)

class EmptyRandomGoalEnv8x8(EmptyEnv):
    def __init__(self):
        super().__init__(size=8, goal_pos=None)

class EmptyEnv10x10(EmptyEnv):
    def __init__(self, **kwargs):
        super().__init__(size=10, **kwargs)

class EmptyRandomGoalEnv10x10(EmptyEnv):
    def __init__(self):
        super().__init__(size=10, goal_pos=None)

class EmptyEnv16x16(EmptyEnv):
    def __init__(self, **kwargs):
        super().__init__(size=16, **kwargs)

class EmptyRandomEnv16x16(EmptyEnv):
    def __init__(self):
        super().__init__(size=16, agent_start_pos=None)

class EmptyRandomRandomGoalEnv16x16(EmptyEnv):
    def __init__(self):
        super().__init__(size=16, agent_start_pos=None, goal_pos=None)

class EmptyRandomGoalEnv16x16(EmptyEnv):
    def __init__(self):
        super().__init__(size=16, goal_pos=None)

class EmptyEnv100x100(EmptyEnv):
    def __init__(self, **kwargs):
        super().__init__(size=100, **kwargs)

class EmptyRandomGoalEnv100x100(EmptyEnv):
    def __init__(self):
        super().__init__(size=100, goal_pos=None)


register(
    id='MiniGrid-Empty-5x5-v0',
    entry_point='gym_minigrid.envs:EmptyEnv5x5'
)

register(
    id='MiniGrid-Empty-Random-5x5-v0',
    entry_point='gym_minigrid.envs:EmptyRandomEnv5x5'
)

register(
    id='MiniGrid-Empty-Random-RandomGoal-5x5-v0',
    entry_point='gym_minigrid.envs:EmptyRandomRandomGoalEnv5x5'
)

register(
    id='MiniGrid-Empty-RandomGoal-5x5-v0',
    entry_point='gym_minigrid.envs:EmptyRandomGoalEnv5x5'
)

register(
    id='MiniGrid-Empty-6x6-v0',
    entry_point='gym_minigrid.envs:EmptyEnv6x6'
)

register(
    id='MiniGrid-Empty-Random-6x6-v0',
    entry_point='gym_minigrid.envs:EmptyRandomEnv6x6'
)


register(
    id='MiniGrid-Empty-Random-RandomGoal-6x6-v0',
    entry_point='gym_minigrid.envs:EmptyRandomRandomGoalEnv6x6'
)

register(
    id='MiniGrid-Empty-RandomGoal-6x6-v0',
    entry_point='gym_minigrid.envs:EmptyRandomGoalEnv6x6'
)

register(
    id='MiniGrid-Empty-8x8-v0',
    entry_point='gym_minigrid.envs:EmptyEnv'
)

register(
    id='MiniGrid-Empty-Random-8x8-v0',
    entry_point='gym_minigrid.envs:EmptyRandomEnv8x8'
)

register(
    id='MiniGrid-Empty-Random-RandomGoal-8x8-v0',
    entry_point='gym_minigrid.envs:EmptyRandomRandomGoalEnv8x8'
)

register(
    id='MiniGrid-Empty-RandomGoal-8x8-v0',
    entry_point='gym_minigrid.envs:EmptyRandomGoalEnv8x8'
)

register(
    id='MiniGrid-Empty-10x10-v0',
    entry_point='gym_minigrid.envs:EmptyEnv10x10'
)

register(
    id='MiniGrid-Empty-RandomGoal-10x10-v0',
    entry_point='gym_minigrid.envs:EmptyRandomGoalEnv10x10'
)

register(
    id='MiniGrid-Empty-16x16-v0',
    entry_point='gym_minigrid.envs:EmptyEnv16x16'
)

register(
    id='MiniGrid-Empty-Random-16x16-v0',
    entry_point='gym_minigrid.envs:EmptyRandomEnv16x16'
)

register(
    id='MiniGrid-Empty-Random-RandomGoal-16x16-v0',
    entry_point='gym_minigrid.envs:EmptyRandomRandomGoalEnv16x16'
)

register(
    id='MiniGrid-Empty-RandomGoal-16x16-v0',
    entry_point='gym_minigrid.envs:EmptyRandomGoalEnv16x16'
)

register(
    id='MiniGrid-Empty-100x100-v0',
    entry_point='gym_minigrid.envs:EmptyEnv100x100'
)

register(
    id='MiniGrid-Empty-RandomGoal-100x100-v0',
    entry_point='gym_minigrid.envs:EmptyRandomGoalEnv100x100'
)
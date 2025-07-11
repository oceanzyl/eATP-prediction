# Example of changing the default optmization schedule
from modeller import *
from modeller.automodel import *

log.verbose()
env = Environ()

# Give less weight to all soft-sphere restraints:
env.schedule_scale = physical.Values(default=1.0, soft_sphere=0.7)
env.io.atom_files_directory = ['/home/oceanzyl1807/Dorn1_prediction/Modeller/MODELLING_test-pipline/pdbs']

a = AutoModel(env, alnfile='p2k1-mult.ali',
                knowns=('1bjqF', '1fatA', '3ipvA'),
                sequence='p2k1',
                assess_methods=(assess.DOPE,
                                assess.normalized_dope,
                                assess.GA341))
a.starting_model = 1
a.ending_model = 10

# Very thorough VTFM optimization:
a.library_schedule = autosched.slow
a.max_var_iterations = 300

# Thorough MD optimization:
a.md_level = refine.slow

# Repeat the whole cycle 2 times and do not stop unless obj.func. > 1E6
a.repeat_optimization = 2
a.max_molpdf = 1e6

a.make()

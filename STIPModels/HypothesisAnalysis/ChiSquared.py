from scipy.stats import chi2_contingency

class ChiSquared() :

    def __init__(self) :
        pass
    
    def calculateChiSquared(self, chiData = []) :

        stat, p, dof, expected = chi2_contingency(chiData)

        print('Stat :',stat)
        print('P :',p)
        print('Degree Of Freedom :',dof)
        print('Expected :', expected)

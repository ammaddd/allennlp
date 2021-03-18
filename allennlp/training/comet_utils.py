try:
    from comet_ml import Experiment
    comet_installed = True
except:
    comet_installed = False


class CometLogger():
    def __init__(self):
        global comet_installed
        self._logging = False
        if comet_installed:
            try:
                self._experiment = Experiment(auto_metric_logging=False)
                self._logging = True
            except:
                print("Comet not configured properly")
        else:
            print("Comet is not installed")
    
    def log_metrics(self, dic, step, epoch):
        if self._logging:
            self._experiment.log_metrics(dic, step=step, epoch=epoch)
    
    def log_parameters(self, dic):
        if self._logging:
            self._experiment.log_parameters(dic)

    def log_model(self, path):
        if self._logging:
            self._experiment.log_model("allennlp", path)

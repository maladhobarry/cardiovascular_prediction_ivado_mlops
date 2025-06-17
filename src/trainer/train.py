from trainer.trainers import RandomForestTrainer, SVMTrainer, LogisticRegressionTrainer


if __name__ == '__main__':
    rf_trainer = RandomForestTrainer()
    rf_trainer.train_random_forest('../../data/processed/clean_data_20240207_114159.csv', '../models/random_forest.pkl')

    # svm_trainer = SVMTrainer()
    # svm_trainer.train_svm('../../data/processed/clean_data_20240207_114159.csv', '../../models/svm.pkl')
    
    # lr_trainer = LogisticRegressionTrainer()
    # lr_trainer.train_logistic_regression('../../data/processed/clean_data_20240207_114159.csv', '../models/logistic_regression.pkl')

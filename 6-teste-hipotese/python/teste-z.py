from statsmodels.stats.proportion import proportions_ztest

# compare 1 mean with a specific value
sample_size = 500
qtt_to_consider = 30
proportion = qtt_to_consider/sample_size

value_to_compare = 0.05

z_stat, p_valor = proportions_ztest(qtt_to_consider, sample_size, value_to_compare, alternative='larger')
print(f'Estatística z: {z_stat:.4f}')
print(f'p-valor: {p_valor:.4f}')


print("------------------------")
# for 2 samples (test A/B)
sample1_size = 2000
sample1_convertions = 180
sample1_proportion = sample1_convertions/sample1_size

sample2_size = 2200
sample2_convertions = 250
sample2_proportion = sample2_convertions/sample2_size

# doesnt need to pass the proportions, it calcs internally
# [qtt_que_forma_nossa_proporcao1, qtt_que_forma_nossa_proporcao2] , [N1, N2]
z_stat, p_valor = proportions_ztest([sample1_convertions, sample2_convertions], [sample1_size, sample2_size]) # by default is bicaudal

print(f'Estatística z: {z_stat:.4f}')
print(f'p-valor: {p_valor:.4f}')

print("------------------------")
# show that the order doesnt care
z_stat, p_valor = proportions_ztest([sample2_convertions, sample1_convertions], [sample2_size, sample1_size]) # by default is bicaudal

print(f'Estatística z: {z_stat:.4f}')
print(f'p-valor: {p_valor:.4f}')


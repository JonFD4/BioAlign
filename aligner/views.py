from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    if request.method == 'POST':
        seq1 = request.POST.get('sequence 1', '').strip()
        seq2 = request.POST.get('sequence 2', '').strip()
        context['seq1'] = seq1
        context['seq2'] = seq2

        context['results'] = f"Sequence 1 length :{len(seq1)}; Sequence 2 lenghth : {len(seq2)}"
    return render(request, 'aligner/home.html', context)
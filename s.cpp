int trap(vector<int> &h)
{
    int n = h.size();

    int left = 0;

    int right = n - 1;

    int res = 0;

    int ml = 0;

    int mr = 0;

    while (left <= right)
    {

        if (h[left] <= h[right])
        {
            if (h[left] >= ml)
            {
                // why res is not added here - think. h[left] doesnt have any water to hold
                ml = h[left];
            }
            else
            {
                res = res + ml - h[left];
            }
            left++;
        }
        else
        {
            if (h[right] >= mr)
            {
                mr = h[right];
            }
            else
            {
                res = res + mr - h[right];
            }
            right--;
        }
    }
    return res;
}
}
;
